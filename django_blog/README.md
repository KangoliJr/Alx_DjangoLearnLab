* **Post List (`/posts/`)**: A `ListView` displays all blog posts. Accessible to all users.
* **Post Detail (`/posts/<int:pk>/`)**: A `DetailView` shows a single post. Accessible to all users. Includes links for editing and deleting if the user is the author.
* **Create Post (`/posts/new/`)**: A `CreateView` with `LoginRequiredMixin` allows authenticated users to create new posts. The author is automatically set to the logged-in user.
* **Update Post (`/posts/<int:pk>/edit/`)**: An `UpdateView` with `LoginRequiredMixin` and `UserPassesTestMixin`. Only the author can edit their own posts.
* **Delete Post (`/posts/<int:pk>/delete/`)**: A `DeleteView` with `LoginRequiredMixin` and `UserPassesTestMixin`. Only the author can delete their own posts.

Permissions
 Creating a post requires a user to be logged in.
 Editing or deleting a post requires the user to be both logged in and the original author of the post. Unauthorized attempts will result in a 403 Forbidden error.