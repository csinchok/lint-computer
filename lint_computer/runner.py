from logan.runner import run_app


def generate_settings():
    """
    This command is run when ``default_path`` doesn't exist, or ``init`` is
    run and returns a string representing the default data to put into their
    settings file.
    """
    return ""


def main():
    run_app(
        project='lint-computer',
        default_config_path='./',
        default_settings='lint_computer.conf.defaults',
        settings_initializer='lint_computer.runner.generate_settings',
        settings_envvar='LINTCOMPUTER_CONF',
    )

if __name__ == '__main__':
    main()
