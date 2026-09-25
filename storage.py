import json


def get_json(filename: str) -> list[dict]:
    with open(filename, "r") as json_read:
        return json.load(json_read)


def save_json(filename: str, file: list[dict]):
    with open(filename, "w") as json_write:
        json_write.write(json.dumps(file, indent=4))


def get_available_id(blogposts: list[dict]):
    used_ids = set([blogpost["id"] for blogpost in blogposts])
    ordered_ids = sorted(used_ids)

    return find_smallest_id(ordered_ids)


def find_smallest_id(ordered_ids: list[int]) -> int:
    expected_id = 1
    for current_id in ordered_ids:
        if expected_id != current_id:
            return expected_id
        expected_id += 1

    return expected_id


def create_new_blogpost(new_post: dict, new_id: int) -> dict:
    return {
        "id": new_id,
        "author": new_post["author"],
        "title": new_post["title"],
        "content": new_post["content"]
    }

def reorder_blogposts_by_id(blog_posts: list[dict]) -> None:
    blog_posts.sort(key=lambda x: x["id"])





