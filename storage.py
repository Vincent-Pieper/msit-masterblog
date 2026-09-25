import json


def get_json(filename: str) -> list[dict]:
    with open(filename, "r", encoding="utf-8") as json_read:
        return json.load(json_read)


def save_json(filename: str, file: list[dict]):
    with open(filename, "w", encoding="utf-8") as json_write:
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


def delete_blogpost_by_id(blog_posts: list[dict], post_id: int) -> None:
    for current_index, post in enumerate(blog_posts, start=0):
        if post["id"] == post_id:
            blog_posts.pop(current_index)
            return


def fetch_blogpost_by_id(blog_posts: list[dict], post_id: int) -> dict[str, int | str] | None:
    for post in blog_posts:
        if post["id"] == post_id:
            return post


def update_blogpost_by_id(blog_posts: list[dict], post_id: int, updates: dict[str, int | str]) -> None:
    for post in blog_posts:
        if post["id"] == post_id:
            for key in updates:
                post[key] = updates[key]
            return


def reorder_blogposts_by_id(blog_posts: list[dict]) -> None:
    blog_posts.sort(key=lambda x: x["id"])





