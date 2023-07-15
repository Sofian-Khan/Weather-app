# OpenAI Image Generation

This is a Node.js application that generates images using the OpenAI API. It provides a simple web interface where users can input a prompt and image size to generate an image.

## Installation

1. Clone the repository:

2. Install the dependencies:

3. Set up environment variables:

Create a `.env` file in the project root directory and add the following variables:

Replace `<your_openai_api_key>` with your OpenAI API key and `<port_number>` with the desired port number for the server.

## Usage

1. Start the server:

2. Open your web browser and go to `http://localhost:<port_number>` (replace `<port_number>` with the port number you specified in the `.env` file).

3. Enter a prompt and select an image size.

4. Click the "Generate Image" button.

5. The generated image will be displayed below the form.

## Project Structure

- `app.js`: Entry point of the application, sets up the Express server and middleware.
- `routes/openaiRoutes.js`: Defines the API routes for the OpenAI functionality.
- `controllers/openaiController.js`: Contains the logic for generating the image using the OpenAI API.
- `public`: Static folder for serving HTML, CSS, and client-side JavaScript files.

## Dependencies

- `express`: Web framework for Node.js.
- `dotenv`: Loads environment variables from a `.env` file.
- `openai`: Official OpenAI API library for Node.js.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).




