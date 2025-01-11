<?php
// Vulnerable code: Blind SQL Injection
$id = $_GET['id'];

$conn = new mysqli("localhost", "root", "", "test_db");
$query = "SELECT * FROM users WHERE id = $id AND 1=1";
$result = $conn->query($query);

if ($result->num_rows > 0) {
    echo "Record exists.";
} else {
    echo "No record found.";
}
?>
