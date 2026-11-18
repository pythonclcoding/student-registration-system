
import os

from app import create_app

app = create_app()

if __name__ == "__main__":
    debug_value = os.getenv(
        "FLASK_DEBUG", "false"
    ).strip().lower()

    if debug_value in {"1", "true", "yes", "on"}:
        debug_mode = True
    elif debug_value in {"0", "false", "no", "off", ""}:
        debug_mode = False
    else:
        raise ValueError(
            f"Invalid FLASK_DEBUG value: {debug_value}"
        )

    app.run(debug=debug_mode)
