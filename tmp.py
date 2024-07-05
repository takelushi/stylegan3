import torch.utils.cpp_extension

module_name = "bias_act_plugin"
cached_build_dir = "C:\\Users\\takelushi\\AppData\\Local\\torch_extensions\\torch_extensions\\Cache\\py38_cu121\\bias_act_plugin\\3cb576a0039689487cfba59279dd6d46-nvidia-geforce-gtx-1080-ti"
verbose_build = True
cached_sources = ['C:\\Users\\takelushi\\AppData\\Local\\torch_extensions\\torch_extensions\\Cache\\py38_cu121\\bias_act_plugin\\3cb576a0039689487cfba59279dd6d46-nvidia-geforce-gtx-1080-ti\\bias_act.cpp', 'C:\\Users\\takelushi\\AppData\\Local\\torch_extensions\\torch_extensions\\Cache\\py38_cu121\\bias_act_plugin\\3cb576a0039689487cfba59279dd6d46-nvidia-geforce-gtx-1080-ti\\bias_act.cu']
build_kwargs = {'extra_cuda_cflags': ['--use_fast_math', '--allow-unsupported-compiler']}



print(module_name, cached_build_dir, verbose_build, cached_sources, build_kwargs)
torch.utils.cpp_extension.load(name=module_name, build_directory=cached_build_dir,
    verbose=verbose_build, sources=cached_sources, **build_kwargs)
