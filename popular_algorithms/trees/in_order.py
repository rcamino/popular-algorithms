def in_order(root, callback):
    if "left" in root:
        in_order(root["left"], callback)

    callback(root["value"])

    if "right" in root:
        in_order(root["right"], callback)
