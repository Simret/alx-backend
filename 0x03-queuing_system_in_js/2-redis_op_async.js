import redis from "redis";
const client = redis.createClient();

client.on("error", (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on("connect", () => {
  console.log("Redis client connected to the server");
});

function setNewSchool(schoolName, value) {
	client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
	await client.get(schoolName, redis.print);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');