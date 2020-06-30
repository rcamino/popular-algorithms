def pre_order(root, callback):
    callback(root["value"])

    if "left" in root:
        pre_order(root["left"], callback)

    if "right" in root:
        pre_order(root["right"], callback)
