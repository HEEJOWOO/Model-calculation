from models import Net
from FLOPs.profile import profile

width = 320
height = 180
model = model = Net(scale_factor=4)
flops, params = profile(model, input_size=(1, 3, height, width))
print('Net_light: {} x {}, flops: {:.10f} GFLOPs, params: {}'.format(height,width,flops/(1e9),params))

