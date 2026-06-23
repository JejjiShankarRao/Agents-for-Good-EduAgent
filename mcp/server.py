from mcp.server.fastmcp import FastMCP

mcp = FastMCP("EduAgent")

@mcp.tool()
def get_course(course_name: str):

    courses = {

        "python": "Python Complete Course",

        "machine learning": "Machine Learning Fundamentals",

        "deep learning": "Deep Learning with TensorFlow",

        "fastapi": "FastAPI for Beginners"

    }

    return courses.get(
        course_name.lower(),
        "Course not found"
    )


if __name__ == "__main__":

    mcp.run()