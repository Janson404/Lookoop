# 2018-12-12
tf.Graph.device() # 指定运行计算的设备
tf.add_to_collection() # 将资源加入一个或多个集合中
tf.get_collection() # 获取一个集合里面的所有资源

result.get_shape() # 获取结果张量的维度信息
tf.Tensor.eval() # 计算一个张量的值
tf.InteractiveSession() # 将生成的会话注册成默认会话

tf.ConfigProto() # 配置需要生成的会话,以下为参数
	# allow_soft_placement: 1.无法在CPU进行计算，2. 没有CPU资源 3. 运算输入包含对CPU计算结果引用
	# log_device_placement: 记录日志

tf.matual() # 元素之间相乘
tf.random_normal([2,3], stddev=2) # 产生一个2x3的矩阵， 各个元素为0，标准差为2的随机数
tf.Variable(weights.initialized_value()) # 用weights来初始化相同值
tf.global_variavles_initializer() # 初始化所有变量
tf.global_variables() # 获取当前计算图的所有变量
tf.trainable_varibles() # 获得所有优化参数
tf.clip_by_value() # 将一个张量中的数值限制在一个范围内
tf.reduce_mean() # 