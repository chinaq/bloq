# 简易 Deploy 于 Windows 上


- [简易 Deploy 于 Windows 上](#简易-deploy-于-windows-上)
    - [目的](#目的)
    - [问题](#问题)
    - [手段](#手段)



## 目的
- 只是想要简单点将本机上开发完成的项目在 windows server 上部署

## 问题
- win 10 之前的 windows 没有默认 ssh ，有点麻烦

## 手段
- 服务端
    - 安装 sshd 使用 ssh 
    - 安装 git 使用 MinGW 环境运行 bash
- 本机使用脚本如下：

``` bash
# publish
echo "---------"
echo "publish"
rm $local_path'-publish'$pub_zip

# zip
echo "---------"
echo "zip files"
7z a $local_path'-publish'$pub_zip $local_path$pub_folder

# upload
echo "---------"
echo "put zip"
sftp $s113:$rpath <<< 'put '$local_path'-publish'$pub_zip

# prepare
killsm='cmd /C "Taskkill /IM SFR.exe /F /FI ^"MEMUSAGE gt 2^" "'
remove='bash.exe -c "rm -rf /e'$rpath$pub_folder'"'
extra='7z x "e:/'$rpath$pub_zip'" -o"e:/'$rpath'"'
copysetting='bash.exe -c "cp /e'$rpath$stfile' /e'$rpath$pub_folder'"'
runsm='bash.exe -c "cd /e'$rpath$pub_folder'; ./SFR.exe'

# do
echo "---------"
echo $killsm
ssh $s113 $killsm

echo "---------"
echo $remove
ssh $s113 $remove

echo "---------"
echo $extra
ssh $s113 $extra

echo "---------"
echo $copysetting
ssh $s113 $copysetting

echo "---------"
echo $runsm
ssh $s113 $runsm

```

