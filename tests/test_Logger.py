def test_logger_constuction():
    from BiomecTrack.LOGGER.Logger import Logger
    import logging

    logger_reference = Logger(logging)

    assert logger_reference is not None


def test_log_into_warning(caplog):
    from BiomecTrack.LOGGER.Logger import Logger
    import logging

    logger_reference = Logger(logging)
    with caplog.at_level(logging.NOTSET):
        logger_reference.log_into_warning("Test warning")
        assert "Test warning" in caplog.text


def test_log_into_info(caplog):
    from BiomecTrack.LOGGER.Logger import Logger
    import logging

    logger_reference = Logger(logging)
    with caplog.at_level(logging.NOTSET):
        logger_reference.log_into_info("Test info")
        assert "Test info" in caplog.text

