from massive import RESTClient
from collections import defaultdict
import http.server
import socketserver
import traceback
import json

# Connect to http://localhost:8889 in your browser to view D3 treemap.
PORT = 8889

# Inline html + js code to render D3.js Treemap
html = """
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
    <title>Massive.com Snapshot + D3.js Treemap</title>
    <script src="https://d3js.org/d3.v6.min.js"></script>
    <style type="text/css">
        svg {
            font: 10px sans-serif;
        }

        .node {
            border: solid 1px white;
            font: 10px sans-serif;
            line-height: 12px;
            overflow: hidden;
            position: absolute;
            text-indent: 2px;
        }
    </style>
</head>
<body>
<div id="treemap"></div>
<script type="text/javascript">
d3.json("/data").then(function(data) {

    const select = d3.select('body').insert('select', 'script')
        .attr('id', 'categorySelector')
        .style('position', 'absolute')
        .style('z-index', '10');

    select.append('option').text('All').attr('value', 'all');

    data.children.forEach(child => {
        select.append('option').text(child.name).attr('value', child.name);
    });

    drawTreemap(data); // Draw the initial treemap with all categories

	d3.select("#categorySelector").on("change", function() {
	    console.log("Dropdown Changed!");
	    const selectedCategory = d3.select(this).property('value');
	    drawTreemap(data, selectedCategory);
	});

}).catch(function(error) {
    console.log(error);
});

function drawTreemap(data, selectedCategory = 'all') {
    d3.select("svg").remove(); // Remove the previous SVG element
    
    var svg = d3.select("body")
        .append("svg")
        .attr("width", 2000)
        .attr("height", 1200)
        .style("font", "14px sans-serif");

    var treemap = d3.treemap()
        .size([2000, 1200])
        .paddingInner(0)
        .paddingOuter(1)
        .paddingTop(25);

    var filteredData = selectedCategory === 'all' ? data : {
        name: data.name,
        children: data.children.filter(child => child.name === selectedCategory)
    };
    
	if(selectedCategory !== 'all') {
	    // Iterate through the children of the selected category
	    filteredData.children.forEach(catChild => {
	        if(catChild.children) {  // Check if the child has its own children (i.e., depth 2 items)
	            catChild.children.forEach(depth2Child => {
	                if(depth2Child.children) {  // Check if this child has its own children (i.e., depth 3 items)
	                    depth2Child.children.forEach(depth3Item => {
	                        // Now, you can modify the weight of each depth 3 item
	                        depth3Item.weight = depth3Item.weight * 2;
	                    });
	                }
	            });
	        }
	    });
	}

    var root = d3.hierarchy(filteredData)
        .sum(function(d) { return Math.pow(d.weight + 1, 1.3); })
        .sort(function(a, b) { return b.height - a.height || b.value - a.value; });

    console.log(filteredData);

	var fontSize = d3.scaleSqrt()
	    .range([10, 20]);  // range of font sizes

    treemap(root);

    fontSize.domain([
        d3.min(root.descendants(), d => (d.x1 - d.x0) * (d.y1 - d.y0)),
        d3.max(root.descendants(), d => (d.x1 - d.x0) * (d.y1 - d.y0))
    ]);

    var cell = svg.selectAll("g")
        .data(root.descendants())
        .enter().append("g")
        .attr("transform", function(d) { return "translate(" + d.x0 + "," + d.y0 + ")"; })
        .attr("id", function(d) { return 'cell-' + d.ancestors().reverse().map(d => d.data.ticker).join("-"); });

	// Remove rectangles for depth 2 items
	cell.filter(function(d) { return d.depth === 2; })
	    .select("rect")
	    .remove();

	// Remove text for depth 2 items
	cell.filter(function(d) { return d.depth === 2; })
	    .select("text")
	    .remove();


	cell.append("rect")
	    .attr("id", function(d) { return 'rect-' + d.data.name; })
	    .attr("fill", function(d) { 
	        //if (d.depth === 0) return "#282828";
	        //if (d.depth === 1) return "#000000";
	        if (d.depth === 2) return colorScale(d.data.change); // symbol box header
	        if (d.depth === 3) return colorScale(d.data.change); // symbol box
	    })
	    .attr("width", function(d) { return d.x1 - d.x0; }) // replace "d" with correct dimensions
	    .attr("height", function(d) { return d.y1 - d.y0; }) // replace "d" with correct dimensions

	// header + symbol text
	cell.append("text")
	    .each(function(d) { 
	        if(selectedCategory !== 'all' && d.depth === 3) {
	            d3.select(this)
	              .attr("x", function(d) { return (d.x1 - d.x0) / 2; }) // Position text in the middle horizontally
	              .attr("y", function(d) { return (d.y1 - d.y0) / 2 - 10; }) // Position text a bit higher to make room for pctChange
	              .attr("text-anchor", "middle") // Center the text
	              .attr("dominant-baseline", "middle") // Vertically align text
	              .style("font", function(d) { return fontSize((d.x1 - d.x0) * (d.y1 - d.y0)) + "px sans-serif"; }) // Increase the font size for children proportional to the rectangle area
	              .style("font-weight", "bold") // Make the font bold
	              .style("pointer-events", "none") // Mouse events will trigger even when you hover over the text, as if the text wasn't there.
	              .attr("fill", "white")
	        } 
	        if(d.depth === 1) {
	            d3.select(this)
	              .attr("x", 4) // Add a bit of padding for the parent and root labels
	              .attr("y", 14) // Position the text a bit lower for the parent and root labels
	              .style("font-weight", "bold") // Make the font bold
	              .style("pointer-events", "none") // Mouse events will trigger even when you hover over the text, as if the text wasn't there.
	              .attr("fill", 'white');
	        }
	    })
	    .text(function(d) { 
	        if(selectedCategory !== 'all' && d.depth === 3) return d.value > 0.1 ? d.data.name : null;
	        if(d.depth === 1) return d.data.name;
	        return null;
	    });

	// % text
	cell.append("text")
	    .each(function(d) { 
	        if(d.depth === 3) { // only for children
	            d3.select(this)
	              .attr("x", function(d) { return (d.x1 - d.x0) / 2; }) // Position text in the middle horizontally
	              .attr("y", function(d) { return (d.y1 - d.y0) / 2 + 10; }) // Position text a bit lower to be under the name
	              .attr("text-anchor", "middle") // Center the text
	              .attr("dominant-baseline", "middle") // Vertically align text
	              .style("font", function(d) { return fontSize((d.x1 - d.x0) * (d.y1 - d.y0)) + "px sans-serif"; }) // Increase the font size for children proportional to the rectangle area
	              .style("pointer-events", "none") // Mouse events will trigger even when you hover over the text, as if the text wasn't there.
	              .attr("fill", "white")
				  .text(function(d) { 
				      if(d.depth <= 1) return null; // Don't render text for root or spacer
				      var area = (d.x1 - d.x0) * (d.y1 - d.y0);
				      return area > 500 ? d.data.change + '%' : null;
				      return d.data.change + '%';
				  });
	        } 
	    });

	function colorScale(value) {
	    if (value <= -2.99) {
	        return "rgb(240, 62, 61)"; // -3+
	    } else if (value <= -1.99) {
	        return "rgb(187, 73, 70)"; // -2 to -3
	    } else if (value <= -0.01) {
	        return "rgb(137, 77, 81)"; // -1 to -2
	    } else if (value < 0.01) {
	        return "rgb(70, 76, 92)";  // -0 to -1
	    } else if (value <= 1.99) { 
	        return "rgb(60, 126, 85)"; // 1-1.99
	    } else if (value <= 2.99) {
	        return "rgb(53, 162, 86)"; // 2-2.99
	    } else {
	        return "rgb(54, 210, 97)"; // 3+
	    }
	}

}
</script>
</body>
</html>
"""


class handler(http.server.SimpleHTTPRequestHandler):
    def generate_data(self):
        client = (
            RESTClient()
        )  # Assuming you have MASSIVE_API_KEY environment variable set up
        snapshots = client.get_snapshot_all("stocks")
        pct_changes = {
            snapshot.ticker: round(snapshot.todays_change_percent, 2)
            for snapshot in snapshots
        }

        with open("sic_code_groups.json", "r") as file:
            sic_code_groups = json.load(file)

        data = defaultdict(lambda: defaultdict(list))

        for sic_code, group_data in sic_code_groups.items():
            parent = group_data["sic_description"]
            for company in group_data["companies"]:
                ticker = company["ticker"]
                weight = company["weight"]
                pct_change = pct_changes.get(ticker, 0.0)
                data[parent][ticker].append(
                    {"name": ticker, "weight": weight, "change": pct_change}
                )

        data = dict(data)
        output = {"name": "root", "children": []}
        for parent, children in data.items():
            parent_dict = {"name": parent, "children": []}
            for child, companies in children.items():
                total_change = sum(company["change"] for company in companies)
                avg_change = total_change / len(companies) if companies else 0
                avg_change = round(avg_change, 2)
                child_dict = {
                    "name": child,
                    "change": avg_change,
                    "children": companies,
                }
                parent_dict["children"].append(child_dict)
            output["children"].append(parent_dict)

        return json.dumps(output)

    def do_GET(self):
        if self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            json_data = self.generate_data()
            self.wfile.write(json_data.encode())
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode())


try:
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\nExiting gracefully...")
