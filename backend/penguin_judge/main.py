from argparse import ArgumentParser, Namespace
from os import sched_getaffinity
from typing import List

from penguin_judge import config, load_config_file


def start_api(args: Namespace, rest: List[str]) -> None:
    from uvicorn.main import main as uvicorn_main

    if args.config:
        load_config_file(args.config, 'api')
    uvicorn_main([f'{__package__}.api:app'] + rest)


def start_worker(args: Namespace, rest: List[str]) -> None:
    from penguin_judge.worker import main as worker_main

    if args.config:
        load_config_file(args.config, 'worker')
    max_processes = config.max_processes
    if max_processes <= 0:
        max_processes = len(sched_getaffinity(0))
    worker_main({}, max_processes)


def main() -> None:
    def add_common_args(parser: ArgumentParser) -> ArgumentParser:
        parser.add_argument('-c', '--config', help='config path')
        return parser

    parser = ArgumentParser()
    subparsers = parser.add_subparsers()

    api_parser = add_common_args(subparsers.add_parser('api', help='API Server'))
    api_parser.set_defaults(start=start_api)

    worker_parser = add_common_args(
        subparsers.add_parser('worker', help='Judge Worker')
    )
    worker_parser.set_defaults(start=start_worker)

    args, rest = parser.parse_known_args()
    if hasattr(args, 'start'):
        args.start(args, rest)
    else:
        parser.print_help()
