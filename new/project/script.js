// Todo App JavaScript module

function addTask(taskDescription) {
  tasks.push({ description: taskDescription, completed: false });
  updateLocalStorage();
  renderTasks();
  taskInput.value = "";
}

function renderTasks() {
  taskList.innerHTML = "";
  tasks.forEach(function (task, index) {
    var li = document.createElement("li");
    li.textContent = task.description;
    li.className = "task-item" + (task.completed ? " completed" : "");
    li.addEventListener("click", function () {
      toggleCompleted(index);
    });
    li.appendChild(createDeleteButton(index));
    taskList.appendChild(li);
  });
}

function toggleCompleted(index) {
  tasks[index].completed = !tasks[index].completed;
  updateLocalStorage();
  renderTasks();
}

function deleteTask(index) {
  tasks.splice(index, 1);
  updateLocalStorage();
  renderTasks();
}

function createDeleteButton(index) {
  var deleteButton = document.createElement("button");
  deleteButton.textContent = "X";
  deleteButton.className = "delete-button";
  deleteButton.addEventListener("click", function (event) {
    event.stopPropagation();
    deleteTask(index);
  });
  return deleteButton;
}

function updateLocalStorage() {
  localStorage.setItem("tasks", JSON.stringify(tasks));
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = {
    addTask,
    renderTasks,
    toggleCompleted,
    deleteTask,
    createDeleteButton,
    updateLocalStorage,
  };
} else {
  document.addEventListener("DOMContentLoaded", function () {
    taskInput = document.getElementById("new-task");
    addButton = document.getElementById("add-task");
    taskList = document.getElementById("task-list");
    tasks = JSON.parse(localStorage.getItem("tasks")) || [];

    addButton.addEventListener("click", function () {
      if (taskInput.value.trim() !== "") {
        addTask(taskInput.value);
      }
    });

    renderTasks();
  });
}
