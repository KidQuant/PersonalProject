-- Active: 1657008265525@@localhost@3306@warzone

SELECT * FROM gamertags;

SELECT * FROM aydan;

UPDATE metaphor SET Date = str_to_date(Date, "%m-%d-%Y");

UPDATE metaphor SET Time = time_format(Time, "%H:%i:%s");

UPDATE gamertags
SET GamerTag = 'Mutex%2311566'
WHERE User = 'MuTex';

SELECT *
FROM icemanissac
Where Mode LIKE '%br_vg_royale_quads%'
ORDER BY Date DESC, Time DESC;

SELECT
SELECT *
FROM bbreadman
WHERE NOT EXISTS (
        SELECT *
        FROM huskerrs
        WHERE (
                bbreadman.MatchID = huskerrs.MatchID
            )
            AND NOT EXISTS (
                SELECT *
                FROM fifakill
                WHERE
                    bbreadman.MatchID = fifakill.MatchID
            )
            OR NOT EXISTS (
                SELECT *
                FROM joewo
                WHERE
                    bbreadman.MatchID = joewo.MatchID
            )
    );

CREATE TABLE
    Crowder(
        MatchID text,
        Mode text,
        Kills int,
        Deaths int,
        KDRatio double,
        LobbyKD double,
        Date text,
        Time text,
        User text
    );

DELETE FROM icemanissac WHERE MatchID = '17253392717770040513';