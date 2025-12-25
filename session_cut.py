past_log = []
fresh = False

def pseudo_reset():
    global fresh
    fresh = True

def gen_reply(u, recall=False):
    global fresh
    c = "\n".join(past_log) if recall else ("[Past logs ignored]" if fresh else "")
    fresh = False
    return f"AI reply({u})\n{c}"

past_log.append("Topic X")
pseudo_reset()
print(gen_reply("New topic"))
print(gen_reply("Check previous", True))
