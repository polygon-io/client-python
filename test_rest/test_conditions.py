from polygon.rest.models import Condition
from base import BaseTest


class ConditionsTest(BaseTest):
    def test_list_conditions(self):
        conditions = [c for c in self.c.list_conditions("stocks")]
        expected = [
            Condition(
                abbreviation=None,
                asset_class="stocks",
                data_types=["trade"],
                description=None,
                exchange=None,
                id=1,
                legacy=None,
                name="Acquisition",
                sip_mapping={"UTP": "A"},
                type="sale_condition",
                update_rules={
                    "consolidated": {
                        "updates_high_low": True,
                        "updates_open_close": True,
                        "updates_volume": True,
                    },
                    "market_center": {
                        "updates_high_low": True,
                        "updates_open_close": True,
                        "updates_volume": True,
                    },
                },
            ),
            Condition(
                abbreviation=None,
                asset_class="stocks",
                data_types=["trade"],
                description=None,
                exchange=None,
                id=2,
                legacy=None,
                name="Average Price Trade",
                sip_mapping={"CTA": "B", "UTP": "W"},
                type="sale_condition",
                update_rules={
                    "consolidated": {
                        "updates_high_low": False,
                        "updates_open_close": False,
                        "updates_volume": True,
                    },
                    "market_center": {
                        "updates_high_low": False,
                        "updates_open_close": False,
                        "updates_volume": True,
                    },
                },
            ),
            Condition(
                abbreviation=None,
                asset_class="stocks",
                data_types=["trade"],
                description=None,
                exchange=None,
                id=3,
                legacy=None,
                name="Automatic Execution",
                sip_mapping={"CTA": "E"},
                type="sale_condition",
                update_rules={
                    "consolidated": {
                        "updates_high_low": True,
                        "updates_open_close": True,
                        "updates_volume": True,
                    },
                    "market_center": {
                        "updates_high_low": True,
                        "updates_open_close": True,
                        "updates_volume": True,
                    },
                },
            ),
            Condition(
                abbreviation=None,
                asset_class="stocks",
                data_types=["trade"],
                description=None,
                exchange=None,
                id=4,
                legacy=None,
                name="Bunched Trade",
                sip_mapping={"UTP": "B"},
                type="sale_condition",
                update_rules={
                    "consolidated": {
                        "updates_high_low": True,
                        "updates_open_close": True,
                        "updates_volume": True,
                    },
                    "market_center": {
                        "updates_high_low": True,
                        "updates_open_close": True,
                        "updates_volume": True,
                    },
                },
            ),
            Condition(
                abbreviation=None,
                asset_class="stocks",
                data_types=["trade"],
                description=None,
                exchange=None,
                id=5,
                legacy=None,
                name="Bunched Sold Trade",
                sip_mapping={"UTP": "G"},
                type="sale_condition",
                update_rules={
                    "consolidated": {
                        "updates_high_low": True,
                        "updates_open_close": False,
                        "updates_volume": True,
                    },
                    "market_center": {
                        "updates_high_low": True,
                        "updates_open_close": False,
                        "updates_volume": True,
                    },
                },
            ),
            Condition(
                abbreviation=None,
                asset_class="stocks",
                data_types=["trade"],
                description=None,
                exchange=None,
                id=6,
                legacy=True,
                name="CAP Election",
                sip_mapping={"CTA": "I"},
                type="sale_condition",
                update_rules={
                    "consolidated": {
                        "updates_high_low": True,
                        "updates_open_close": True,
                        "updates_volume": True,
                    },
                    "market_center": {
                        "updates_high_low": True,
                        "updates_open_close": True,
                        "updates_volume": True,
                    },
                },
            ),
            Condition(
                abbreviation=None,
                asset_class="stocks",
                data_types=["trade"],
                description=None,
                exchange=None,
                id=7,
                legacy=None,
                name="Cash Sale",
                sip_mapping={"CTA": "C", "UTP": "C"},
                type="sale_condition",
                update_rules={
                    "consolidated": {
                        "updates_high_low": False,
                        "updates_open_close": False,
                        "updates_volume": True,
                    },
                    "market_center": {
                        "updates_high_low": False,
                        "updates_open_close": False,
                        "updates_volume": True,
                    },
                },
            ),
            Condition(
                abbreviation=None,
                asset_class="stocks",
                data_types=["trade"],
                description=None,
                exchange=None,
                id=8,
                legacy=None,
                name="Closing Prints",
                sip_mapping={"UTP": "6"},
                type="sale_condition",
                update_rules={
                    "consolidated": {
                        "updates_high_low": True,
                        "updates_open_close": True,
                        "updates_volume": True,
                    },
                    "market_center": {
                        "updates_high_low": True,
                        "updates_open_close": True,
                        "updates_volume": True,
                    },
                },
            ),
            Condition(
                abbreviation=None,
                asset_class="stocks",
                data_types=["trade"],
                description=None,
                exchange=None,
                id=9,
                legacy=None,
                name="Cross Trade",
                sip_mapping={"CTA": "X", "UTP": "X"},
                type="sale_condition",
                update_rules={
                    "consolidated": {
                        "updates_high_low": True,
                        "updates_open_close": True,
                        "updates_volume": True,
                    },
                    "market_center": {
                        "updates_high_low": True,
                        "updates_open_close": True,
                        "updates_volume": True,
                    },
                },
            ),
            Condition(
                abbreviation=None,
                asset_class="stocks",
                data_types=["trade"],
                description=None,
                exchange=None,
                id=10,
                legacy=None,
                name="Derivatively Priced",
                sip_mapping={"CTA": "4", "UTP": "4"},
                type="sale_condition",
                update_rules={
                    "consolidated": {
                        "updates_high_low": True,
                        "updates_open_close": False,
                        "updates_volume": True,
                    },
                    "market_center": {
                        "updates_high_low": True,
                        "updates_open_close": False,
                        "updates_volume": True,
                    },
                },
            ),
        ]
        self.assertEqual(conditions, expected)
