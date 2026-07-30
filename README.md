## freeCodeCamp Learning

This repository is intended to document my learning journey on freeCodeCamp, including:

- responsive web design
- JavaScript
- React: a front-end framework
- Python 
- Relational Database
- Back-end development
- ...

I mainly use this space to document some code from my learning process and files needed for certification exams.


### Some skills

由于国内连接 github 不是很稳定, 可以使用代理服务进行 github 的仓库同步：

- git 设置代理服务 `http.proxy` 和 `https.proxy`
	
	- 假设代理服务地址为: `192.168.1.3:6666`
		
		```sh
		# 如果要进行全局设置需要加上 --global 选项
		git config http.proxy http://192.168.1.3:6666
		git config https.proxy http://192.168.1.3:6666
		```

	- 带认证的代理服务设置
		
		```sh
		git config --global http.proxy http://用户名:密码@proxy.example.com:6666
		```

	- 取消代理服务设置
		
		```sh
		# 如果设置的时候使用了 --global, 这里也需要带上 --global 选项
		git config --unset http.proxy
		git config --unset https.proxy
		```
- 通过环境变量设置
	
	临时环境变量设置，只在当前环境中生效，更适合一次性的操作

	```sh
	# MacOS or Linux or git bash
	export HTTP_PROXY=http://proxy.example.com:port
	export HTTPS_PROXY=http://proxy.example.com:port

	# Windows CMD
	set HTTP_PROXY=http://proxy.example.com:8080
	set HTTPS_PROXY=http://proxy.example.com:8080
	```
