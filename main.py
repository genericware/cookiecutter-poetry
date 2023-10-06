import argparse
import asyncio
import sys
from pathlib import Path
import logging

from dotenv import find_dotenv
from pydantic import Field
from pydantic_settings import SettingsConfigDict

logger = logging.getLogger(__name__)


class Settings:

    debug: bool = Field(True, description="Enables debugging mode.")

    model_config = SettingsConfigDict(
        env_file=find_dotenv(".env.local")
    )


async def main(settings: Settings, outpath: Path) -> int:
    ec = 0

    try:
        ...
    except Exception:
        logger.error("an error occurred", exc_info=True)
        ec = 1

    return ec

if __name__ == "__main__":
    # config
    config = Settings()

    # argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", type=str, required=True)
    parser.add_argument("--out-dir", type=str, required=True)
    argv = parser.parse_args()

    # pathlib
    fp = Path(argv.filename)
    op = Path(argv.out_dir)
    if not op.is_dir():
        op.mkdir(parents=True, exist_ok=True)

    # logging
    logging.basicConfig(
        level=logging.DEBUG if config.debug else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[logging.FileHandler(op / f"{fp.stem}.log"), logging.StreamHandler()]
    )

    # run
    main_coro = main(settings=config, outpath=op)
    main_result = asyncio.run(main=main_coro, debug=config.debug)
    sys.exit(main_result)
