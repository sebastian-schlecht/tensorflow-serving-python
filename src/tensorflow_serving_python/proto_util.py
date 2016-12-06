def copy_message(src, dst):
    """
    Copy the contents of a src proto message to a destination proto message via string serialization
    :param src: Source proto
    :param dst: Destination proto
    :return:
    """
    dst.ParseFromString(src.SerializeToString())
    return dst
