# HTTP Server

A basic HTTP server implementation in Python using TCP protocol for Socket communication. This server is able to handle GET and POST requests

## Requirements

- Python 3.x

## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/simple-http-server.git
   ```

2. Navigate to the directory containing the `main.py` file:

   ```bash
   cd http-server
   ```

3. Run the server:

   ```bash
   python main.py
   ```

4. The HTTP server will run on port 4221. You can check for server connection by running
   the following command on a different terminal.

   ```bash
   nc -vz 127.0.0.1 4221
   ```

5. To perform a POST request, make sure the server is running and on a different terminal run
   the following command.

   ```bash
   curl -vvv -d "Greetings from the second terminal" localhost:4221/files/readme.txt
   ```

   You should see a new file "readme.txt" created in your project directory with the content as the content being passed in the POST request.

## Customization

- You can customize the behavior of the server by modifying the `main.py` file. For example, you can add support for other HTTP methods, or implement additional functionality.
