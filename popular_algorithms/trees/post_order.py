def post_order(root, callback):
    if "left" in root:
        post_order(root["left"], callback)

    if "right" in root:
        post_order(root["right"], callback)

    callback(root["value"])
