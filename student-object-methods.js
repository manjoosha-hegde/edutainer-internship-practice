let student = {
    name: "Manjoosha Ganapati Hegde",
    college: "Don Bosco Institute of Technology",
    course: "Information Science and Engineering",
    semester: 8,
    role: "Junior Software Developer Intern",

    introduce: function() {
        console.log("Hello, my name is " + this.name);
    },

    showCollege: function() {
        console.log("I study at " + this.college);
    },

    showCourse: function() {
        console.log("My course is " + this.course);
    }
};

student.introduce();
student.showCollege();
student.showCourse();
