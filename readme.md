# Media Hub v 2

Media Hub is a transcoding workflow tool that produces Video On Demand (VOD) ready packages based on a clients requirements. For example if your client requires a .tar containing a 10 Mbps MP4, Cablelabs xml and 2 Image; media Hub will enable you to do this.

This is all controlled by a web based GUI which allows users to easily trigger jobs and get feedback as to which stage of the workflow their task is currently at.

## Requirements
* Python 3.5.2
* Django 1.10
* PostgreSQL 9.6

## Installation

## Configuration

![media_hub.png](https://bitbucket.org/repo/q57yRX/images/4222997962-media_hub.png)

This diagram depicts the basic single transcode server set up.

The core of this configuration consists of the following servers:

* 1 web server that hosts the web GUI website and creates the task XML.
* 1 VM / server running the task_controller.py.
* 1 server running 4 instances of the transcode_controller.py shell script.
* A fibre attached SAN where all media processing takes place. The SAN is also the media repository and temporary location for packages waiting to be delivered.
* A MySQL database which stores all task, video and transcode profile information.
* Connection to the databases that contain TX asset information and asset EPG metadata ( XT database & Schedule database).

### Workflow Overview

1. User submits job in web GUI. Transcode.php creates task XML named as TASKID-PROFILE-TIMESTAMP.xml in the /prep/ DIR on the SAN.
2. Task_controller.py polls the /prep/ DIR looking for new .xml files. If one is found task_prep.py is called. Task_prep.py parses the task XML, checks the /repo/ DIR to see if a file matches the material_id element. If it does the file is copied into the /prep/ DIR and renamed to match the task XML.

    If the file is missing from /repo/ DIR task_prep.py will check the TX Database for the requested asset, if its found the required data is imported into the MySQL database, the file is located on the TX NAS and copied into the /repo/ DIR on the SAN where it is copied to the /prep/ DIR.

    With the video file and task XML now in the /prep/ DIR task_prep.py checks the transcode node watch folders and moves both files into the DIR with the lowest number of files in.
3. Each Transcode_controller.py shell script monitors a DIR and waits for an XML and Video file that share the same name. Once this condition is met transcode_engine.py is invoked and the core transcoding process begins.

4. For this example we are using FFMPEG to do our transcoding. This consists of 2 stages conform and the final transcode to the clients video spec. This process also creates the required metadata, creates the delivery package and places that package in a DIR for QC or delivery.