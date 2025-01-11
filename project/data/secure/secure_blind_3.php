<?php
// Secure code: Prepared statements for Blind SQL Injection
$id = $_GET['id'];

$conn = new mysqli("localhost", "root", "", "test_db");
$query = $conn->prepare("SELECT * FROM users WHERE id = ?");
$query->bind_param("i", $id);
$query->execute();
$result = $query->get_result();

if ($result->num_rows > 0) {
    echo "Record exists.";
} else {
    echo "No record found.";
}
?>
