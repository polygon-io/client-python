import argparse


def is_trace() -> bool:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--trace-api-calls", action="store_true", help="Display API call details"
    )
    args, _ = parser.parse_known_args()
    return args.trace_api_calls
