CREATE TABLE users(
    id INTEGER AUTO_INCREMENT,
    staff_number INTEGER NOT NULL UNIQUE,
    user_name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role INTEGER NOT NULL,
    department VARCHAR(255),
    PRIMARY KEY (id)
);

CREATE TABLE attendance(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    staff_number INTEGER NOT NULL,
    month CHAR(6) NOT NULL,
    overtime_hours DECIMAL(4,1),
    meal_allowance_times INTEGER,
    time_off_hours DECIMAL(4,1),
    work_outside_times INTEGER,
    personal_leave_days DECIMAL(4,1),
    sick_leave_days DECIMAL(4,1),
    marriage_leave_days INTEGER,
    maternity_leave_days INTEGER,
    official_leave_days DECIMAL(4,1),
    exception_times INTEGER,
    FOREIGN KEY (staff_number) REFERENCES users (staff_number)
);

CREATE TABLE leave_details(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    attendance_id INTEGER NOT NULL,
    time_off_dates TEXT,
    work_outside_dates TEXT,
    work_outside_reason VARCHAR(255),
    personal_leave_dates TEXT,
    personal_leave_reason VARCHAR(255),
    sick_leave_dates TEXT,
    sick_leave_reason VARCHAR(255),
    marriage_leave_dates TEXT,
    maternity_leave_dates TEXT,
    official_leave_dates TEXT,
    official_leave_reason VARCHAR(255),
    exception_dates TEXT,
    exception_reason VARCHAR(255),
    FOREIGN KEY (attendance_id) REFERENCES attendance (id)
);


INSERT INTO users(id,staff_number,user_name,password,role,department)
VALUES (9999,9999,'root','12345zxcvb',0,NULL);


