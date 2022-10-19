SELECT round( ((count(email_id)::numeric)/(Select count(*) from emails)),2) as confirm_rate   FROM texts
where signup_action='Confirmed';

######################################

WITH rate AS (
SELECT
  user_id,
  CASE WHEN texts.email_id IS NOT NULL THEN 1
    ELSE 0 END AS signup
FROM emails
LEFT JOIN texts
  ON emails.email_id = texts.email_id
  AND signup_action = 'Confirmed')
  
SELECT ROUND(SUM(signup)::DECIMAL / COUNT(user_id), 2) AS confirmation_rate
FROM rate;