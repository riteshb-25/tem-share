const {
  addTask,
  renderTasks,
  toggleCompleted,
  deleteTask,
  createDeleteButton,
  updateLocalStorage,
  tasks,
} = require("../script");

global.document = {
  getElementById: jest.fn((id) => {
    if (id === "new-task") {
      return { value: "", addEventListener: jest.fn() };
    } else if (id === "add-task") {
      return { addEventListener: jest.fn() };
    } else if (id === "task-list") {
      return { innerHTML: "", appendChild: jest.fn() };
    }
    return null;
  }),
  createElement: jest.fn(() => ({
    textContent: "",
    className: "",
    addEventListener: jest.fn(),
    appendChild: jest.fn(),
  })),
  body: { innerHTML: "" },
};

global.localStorage = {
  getItem: jest.fn(() => JSON.stringify([])),
  setItem: jest.fn(),
};

describe("Todo App", () => {
  beforeEach(() => {
    // Reset the DOM and localStorage mocks before each test
    document.getElementById.mockClear();
    localStorage.getItem.mockClear().mockReturnValue(JSON.stringify([]));
    localStorage.setItem.mockClear();
  });

  test("should add a new task to the list", () => {
    const newTask = "New Task";
    addTask(newTask);
    // Expect the task to be added to the tasks array
    expect(tasks).toEqual([{ description: newTask, completed: false }]);
    // Expect localStorage to be updated with the new task
    expect(localStorage.setItem).toHaveBeenCalledWith(
      "tasks",
      JSON.stringify(tasks)
    );
  });

  // Other tests...
});
