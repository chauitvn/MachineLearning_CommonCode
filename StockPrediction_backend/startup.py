import configargparse
from engine import Engine


def main():
    engine = Engine()
    engine.run()


# Press the green button in the gutter to run the script
if __name__ == '__main__':
    arg_parser = configargparse.get_argument_parser()
    arg_parser.add('-c', '--config', is_config_file=True, help='config file path', default='StockPrediction_backend//config.ini')
    args = arg_parser.parse_known_args()[0]
    main()