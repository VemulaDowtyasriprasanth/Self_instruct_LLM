<?php
// Vulnerable code: Unsanitized input in search query
$search = $_GET['search'];

$conn = new mysqli("localhost", "root", "", "test_db");
$query = "SELECT * FROM products WHERE name LIKE '%$search%'";
$result = $conn->query($query);

while ($row = $result->fetch_assoc()) {
    echo $row['name'];
}
?>
