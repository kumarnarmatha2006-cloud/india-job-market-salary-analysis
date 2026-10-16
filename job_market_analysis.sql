-- =========================================
-- SECTION 1: DATABASE AND TABLE CREATION
-- =========================================

CREATE DATABASE job_market_analysis;

USE job_market_analysis;

CREATE TABLE job_market_data (
    job_id INT PRIMARY KEY,
    job_title VARCHAR(100),
    company_name VARCHAR(150),
    location VARCHAR(100),
    experience_required_years INT,
    skills TEXT,
    salary_min_inr DECIMAL(15,2),
    salary_max_inr DECIMAL(15,2),
    employment_type VARCHAR(50),
    remote_option VARCHAR(50)
);

-- =========================================
-- SECTION 2: BASIC DATA EXPLORATION
-- =========================================

SELECT COUNT(*) AS total_records
FROM job_market_data;

SELECT *
FROM job_market_data
LIMIT 10;

SELECT DISTINCT job_title
FROM job_market_data;

-- =========================================
-- SECTION 3: JOB MARKET ANALYSIS
-- =========================================

SELECT
    job_title,
    COUNT(*) AS total_jobs
FROM job_market_data
GROUP BY job_title
ORDER BY total_jobs DESC;

SELECT
    location,
    COUNT(*) AS total_jobs
FROM job_market_data
GROUP BY location
ORDER BY total_jobs DESC;

SELECT
    employment_type,
    COUNT(*) AS total_jobs
FROM job_market_data
GROUP BY employment_type
ORDER BY total_jobs DESC;

SELECT
    remote_option,
    COUNT(*) AS total_jobs
FROM job_market_data
GROUP BY remote_option
ORDER BY total_jobs DESC;

-- =========================================
-- SECTION 4: SALARY ANALYSIS
-- =========================================

SELECT
    job_title,
    company_name,
    location,
    salary_min_inr,
    salary_max_inr
FROM job_market_data
ORDER BY salary_max_inr DESC
LIMIT 10;

SELECT
    job_title,
    ROUND(AVG((salary_min_inr + salary_max_inr) / 2), 2)
        AS average_salary_midpoint
FROM job_market_data
GROUP BY job_title
ORDER BY average_salary_midpoint DESC;

SELECT
    job_title,
    company_name,
    location,
    salary_max_inr
FROM job_market_data
WHERE salary_max_inr > 1500000
ORDER BY salary_max_inr DESC;

-- =========================================
-- SECTION 5: JOB FILTERING
-- =========================================

SELECT *
FROM job_market_data
WHERE job_title = 'Data Analyst';

SELECT
    job_title,
    company_name,
    location,
    salary_min_inr,
    salary_max_inr
FROM job_market_data
WHERE job_title = 'Data Analyst'
  AND location = 'Bangalore';

SELECT
    job_title,
    company_name,
    location
FROM job_market_data
WHERE job_title = 'Data Analyst'
   OR job_title = 'Data Scientist';

   -- =========================================
-- SECTION 6: ADVANCED SQL ANALYSIS
-- =========================================

SELECT
    job_title,
    COUNT(*) AS total_jobs
FROM job_market_data
GROUP BY job_title
HAVING COUNT(*) > 1000
ORDER BY total_jobs DESC;

-- =========================================
-- SECTION 7: SKILLS ANALYSIS
-- =========================================

SELECT skills
FROM job_market_data
LIMIT 20;

SELECT
    job_title,
    company_name,
    location,
    skills
FROM job_market_data
WHERE LOWER(skills) LIKE '%python%';

SELECT
    job_title,
    COUNT(*) AS total_jobs
FROM job_market_data
WHERE LOWER(skills) LIKE '%sql%'
GROUP BY job_title
ORDER BY total_jobs DESC;