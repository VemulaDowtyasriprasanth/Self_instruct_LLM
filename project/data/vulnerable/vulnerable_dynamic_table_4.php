<?php
// Vulnerable code: Dynamic table name based on user input
$table = $_GET['table'];

$conn = new mysqli("localhost", "root", "", "test_db");
$query = "SELECT * FROM $table";
$result = $conn->query($query);

while ($row = $result->fetch_assoc()) {
    print_r($row);
}
?>
    