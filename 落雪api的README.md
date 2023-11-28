# maimai-prober

An HTTP proxy, API and frontend web server for player to crawl, query and manage their own data from wahlap.com.

## API Reference

Authentication header is required for all API requests: `Authorization: {DeveloperApiKey}`

### POST /api/v0/player

Update player's data.

#### Request Body

Player's data in JSON format.

| Name              | Type                | Description                    |
|-------------------|---------------------|--------------------------------|
| `name`            | `string`            | Player's name                  |
| `rating`          | `int`               | Player's rating                |
| `friend_code`     | `int`               | Player's friend code           |
| `trophy`          | [`Trophy`](#Trophy) | Player's trophy                |
| `course_rank`     | `int`               | Player's course rank           |
| `class_rank`      | `int`               | Player's class rank            |
| `star`            | `int`               | Player's star                  |
| `icon_url`        | `string`            | Player's icon image URL        |
| `rating_rank_url` | `string`            | Player's rating rank image URL |
| `course_rank_url` | `string`            | Player's course rank image URL |
| `class_rank_url`  | `string`            | Player's class rank image URL  |

### GET /api/v0/player/:friend_code

Get player's cached data in JSON format: [`Player`](#Player).

### GET /api/v0/player/qq/:qq

Get player's cached data in JSON format by QQ: [`Player`](#Player).

### GET /api/v0/player/:friend_code/best

Get player's cached best score.

#### Query Parameters

| Name          | Type                        | Description                         |
|---------------|-----------------------------|-------------------------------------|
| `song_id`     | `int`                       | Song ID (conflict with `song_name`) |
| `song_name`   | `string`                    | Song name (conflict with `song_id`) |
| `level_index` | [`LevelIndex`](#LevelIndex) | Level index (or difficulty)         |
| `song_type`   | [`SongType`](#SongType)     | Song type                           |

### GET /api/v0/player/:friend_code/bests

Get player's cached best 50.

### GET /api/v0/player/:friend_code/bests

Get player's cached best scores in different difficulties of single song.

#### Query Parameters

| Name        | Type                    | Description                         |
|-------------|-------------------------|-------------------------------------|
| `song_id`   | `int`                   | Song ID (conflict with `song_name`) |
| `song_name` | `string`                | Song name (conflict with `song_id`) |
| `song_type` | [`SongType`](#SongType) | Song type                           |

### POST /api/v0/player/:friend_code/scores

Update player's scores.

#### Request Body

Player's scores in JSON format.

| Name     | Type                | Description     |
|----------|---------------------|-----------------|
| `scores` | [`Score[]`](#Score) | Player's scores |

### Get /api/v0/player/:friend_code/plate/:plate_id

Get player's plate progress in JSON format: [`Plate`](#Plate).

### GET /api/v0/song/list

Get song list in JSON format: [`Song[]`](#Song).

### GET /api/v0/plate/list

Get plate list in JSON format: [`Plate[]`](#Plate).

## Objects

### LevelIndex

Value for level index (or difficulty).

| Value | Type  | Description |
|-------|-------|-------------|
| `0`   | `int` | Basic       |
| `1`   | `int` | Advanced    |
| `2`   | `int` | Expert      |
| `3`   | `int` | Master      |
| `4`   | `int` | Re:MASTER   |

### SongType

Value for song type.

| Value      | Type     | Description |
|------------|----------|-------------|
| `standard` | `string` | Standard    |
| `dx`       | `string` | Deluxe      |

### Trophy

Trophy object.

| Name    | Type                          | Description  |
|---------|-------------------------------|--------------|
| `name`  | `string`                      | Trophy name  |
| `color` | [`TrophyColor`](#TrophyColor) | Trophy color |

### TrophyColor

Value for trophy color.

| Value     | Type     | Description |
|-----------|----------|-------------|
| `Bronze`  | `string` | Bronze      |
| `Gold`    | `string` | Gold        |
| `Normal`  | `string` | Normal      |
| `Rainbow` | `string` | Rainbow     |
| `Silver`  | `string` | Silver      |

### Score

Score object.

| Name           | Type                              | Description                 |
|----------------|-----------------------------------|-----------------------------|
| `id`           | `int`                             | Song ID                     |
| `song_name`    | `string`                          | Song name                   |
| `level`        | `string`                          | Level                       |
| `level_index`  | `int`                             | Level index (or difficulty) |
| `achievements` | `float`                           | Achievements                |
| `fc`           | [`FullComboType`](#FullComboType) | Full combo type (optional)  |
| `fs`           | [`FullSyncType`](#FullSyncType)   | Full sync type (optional)   |
| `dx_score`     | `int`                             | Deluxe score                |
| `dx_rating`    | `float`                           | Deluxe rating               |
| `rate`         | [`RateType`](#RateType)           | Rate                        |
| `type`         | [`SongType`](#SongType)           | Song type                   |

### Song

Song object.

| Name           | Type                                    | Description       |
|----------------|-----------------------------------------|-------------------|
| `id`           | `int`                                   | Song ID           |
| `title`        | `string`                                | Song title        |
| `artist`       | `string`                                | Song artist       |
| `genre`        | `string`                                | Song genre        |
| `bpm`          | `int`                                   | Song BPM          |
| `version`      | `int`                                   | Song version      |
| `difficulties` | [`SongDifficulties`](#SongDifficulties) | Song difficulties |

### SongDifficulties

Song difficulties object.

| Name       | Type                                  | Description           |
|------------|---------------------------------------|-----------------------|
| `standard` | [`SongDifficulty[]`](#SongDifficulty) | Standard difficulties |
| `dx`       | [`SongDifficulty[]`](#SongDifficulty) | Deluxe difficulties   |

### SongDifficulty

Song difficulty object.

| Name            | Type     | Description   |
|-----------------|----------|---------------|
| `type`          | `string` | Difficulty    |
| `difficulty`    | `int`    | Difficulty    |
| `level`         | `string` | Level         |
| `level_value`   | `float`  | Level value   |
| `note_designer` | `string` | Note designer |
| `version`       | `int`    | Version       |

### Plate

Plate object.

| Name          | Type                                | Description       |
|---------------|-------------------------------------|-------------------|
| `id`          | `int`                               | Plate ID          |
| `name`        | `string`                            | Plate name        |
| `description` | `string`                            | Plate description |
| `required`    | [`PlateRequired[]`](#PlateRequired) | Required          |

### PlateRequired

Plate required object.

| Name           | Type                                         | Description                          |
|----------------|----------------------------------------------|--------------------------------------|
| `difficulties` | `int[]`                                      | Required difficulties (optional)     |
| `rate`         | [`RateType`](#RateType)                      | Required rate (optional)             |
| `fc`           | [`FullComboType`](#FullComboType)            | Required full combo type (optional)  |
| `fs`           | [`FullSyncType`](#FullSyncType)              | Required full sync type (optional)   |
| `songs`        | [`PlateRequiredSongs[]`](#PlateRequiredSong) | Required songs (optional)            |
| `completed`    | `bool`                                       | Is required all completed (optional) |

### PlateRequiredSong

Plate required song object.

| Name                     | Type     | Description                                     |
|--------------------------|----------|-------------------------------------------------|
| `id`                     | `int`    | Song ID                                         |
| `title`                  | `string` | Song title                                      |
| `completed`              | `bool`   | Is required song completed (optional)           |
| `completed_difficulties` | `int[]`  | Required song completed difficulties (optional) |

### FullComboType

Value for full combo type.

| Value | Type     | Description |
|-------|----------|-------------|
| `fc`  | `string` | FC          |
| `fcp` | `string` | FC+         |
| `ap`  | `string` | AP          |
| `app` | `string` | AP+         |

### FullSyncType

Value for full sync type.

| Value  | Type     | Description |
|--------|----------|-------------|
| `fs`   | `string` | FS          |
| `fsp`  | `string` | FS+         |
| `fsd`  | `string` | FSD         |
| `fsdp` | `string` | FSD+        |

### RateType

Value for rate type.

| Value  | Type     | Description |
|--------|----------|-------------|
| `sssp` | `string` | SSS+        |
| `sss`  | `string` | SSS         |
| `ssp`  | `string` | SS+         |
| `ss`   | `string` | SS          |
| `sp`   | `string` | S+          |
| `s`    | `string` | S           |
| `aaa`  | `string` | AAA         |
| `aa`   | `string` | AA          |
| `a`    | `string` | A           |
| `bbb`  | `string` | BBB         |
| `bb`   | `string` | BB          |
| `b`    | `string` | B           |
| `c`    | `string` | C           |
| `d`    | `string` | D           |