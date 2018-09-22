<?php

$defaultdata = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");

function xor_encrypt($in, $key) {
	        $text = $in;
	        $outText = '';

		//Iterate through each character
		for($i=0;$i<strlen($text);$i++) {
		$outText .= $text[$i] ^ $key[$i % strlen($key)];
   		}

		return $outText;
}

$plaintext = json_encode($defaultdata);
$key = 'qw8J';

#echo(xor_encrypt($plaintext, $ciphertext));
$good_data = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");
$good_plaintext = json_encode($good_data);
$good_ciphertext = xor_encrypt( $good_plaintext, $key);
$cookie = base64_encode($good_ciphertext);

echo($cookie);

?>
