<?php
// Vulnerable code: Union-Based SQL Injection
$id = $_GET['id'];

$conn = new mysqli("localhost", "root", "", "test_db");
$query = "SELECT name FROM users WHERE id = $id";
$result = $conn->query($query);

while ($row = $result->fetch_assoc()) {
    echo $row['name'];
}
?>
