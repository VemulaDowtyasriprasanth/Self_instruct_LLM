<?php
// Secure code: Validates table names with a whitelist
$table = $_GET['table'];
$allowed_tables = ['users', 'orders', 'products'];

if (!in_array($table, $allowed_tables)) {
    die("Invalid table name");
}

$conn = new mysqli("localhost", "root", "", "test_db");
$query = "SELECT * FROM $table";
$result = $conn->query($query);

while ($row = $result->fetch_assoc()) {
    print_r($row);
}
?>
