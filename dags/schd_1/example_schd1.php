<?php
try {
	//	SLA:
	//	Usecase ini akan dijalankan otomatis oleh sistem setiap jam 6:00 12:00 & 20:00
	ini_set('max_execution_time', 2000);
	$url = "https://blockchain.info/sadasdsa/1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa";

	$stream_opts = [
		"ssl" => [
			"verify_peer" => false,
			"verify_peer_name" => false,
		]
	];

	$result = file_get_contents($url, false, stream_context_create($stream_opts));

	if (!$result) {
		throw new Exception('An error occurred while fetching URL');
	}

	echo "This scheduler run successfuly";
	exit(0); // Exit with status code 0 to indicate success
} catch (err) {
	echo "Error: " . $e->getMessage();
	exit(1); // Exit with status code 1 to indicate an error
}

?>