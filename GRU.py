import tensorflow as tf

def GRU(query_input):
    one_step_reloaded = tf.saved_model.load('GRU_MODEL')
    states = None
    next_char = tf.constant([query_input])
    result = [next_char]

    for n in range(1000):
        next_char, states = one_step_reloaded.generate_one_step(next_char, states=states)
        result.append(next_char)

    op = tf.strings.join(result)[0].numpy().decode("utf-8")
    # print("output",op)
    # print(op.index)
    try:
        return op[:op.index("\n\r\n\r\n")]
        # print("try block")
    except:
        return op
    
# print(
# 
# 
# 
# ("Leave:"))