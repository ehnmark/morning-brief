import argparse
import yaml
import sys
import logging
from datetime import datetime

def get_config():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="YAML config file", default="config.yaml")
    parser.add_argument("--date", help="Date in yyyy-MM-dd format", default=datetime.now().strftime("%Y-%m-%d"))
    parser.add_argument("--debug", help="Enable debug logging", action="store_true")
    args = parser.parse_args()

    log_level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
        force=True
    )

    # Mute noisy loggers
    if not args.debug:
        logging.getLogger("agent_framework").setLevel(logging.WARNING)
        logging.getLogger("azure").setLevel(logging.WARNING)
        logging.getLogger("httpx").setLevel(logging.WARNING)
    
    try:
        with open(args.config, 'r') as f:
            config = yaml.safe_load(f)
    except Exception as e:
        logging.error(f"Error parsing config file: {e}")
        sys.exit(1)
        
    config['date'] = args.date
    return config
