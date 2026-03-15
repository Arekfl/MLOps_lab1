import os
import argparse
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:
    env_files = {
        "dev": ".env.dev",
        "test": ".env.test",
        "prod": ".env.prod",
    }

    if environment not in env_files:
        raise ValueError("environment must be one of: dev, test, prod")

    config_dir = os.path.join(os.path.dirname(__file__), "config")
    dotenv_path = os.path.join(config_dir, env_files[environment])

    if not os.path.exists(dotenv_path):
        raise FileNotFoundError(f"Missing dotenv file: {dotenv_path}")

    load_dotenv(dotenv_path=dotenv_path, override=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)

    settings = Settings()  # type: ignore

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
