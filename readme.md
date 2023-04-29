## AppleHealthDataToJSON

- Everybody needs mock data when developing for apple health products. Unfortunately, it's hard to come by this data. My solution? Import my own apple health data, then convert it into a usable format.
- This is a package to take that apple healthkit XML and turn it into usable JSON. The script also allows for you to convert the data into useable javascript objects.
- It takes about 2 minutes to set up. The script itself can vary in time, depending on the amount of data you are using.

### Setup

1. Export your apple health data.
   - Open the Health app
   - On the top right, click your profile icon
   - Scroll all the way down, click the `Export All Health Data` button
   - Hit Export and the app will create a .Zip file containing XML data you will need.
   - Get this ZIP to your laptop. Airdrop, email, dropbox, whatever.
2. Install the scripts
   - `git clone https://github.com/sudomichael/AppleHealthDataToJSON.git`
   - `cd AppleHealthDataToJSON`
3. Open your apple health data ZIP, add the .XML data to the root directory of AppleHealthDataToJSON.
4. **Rename the XML file is to `export.xml` if it isn't already**

### Running

##### To convert the XML to usable JavaScript objects

- `python3 main.py`
- Copy the `data` directory in to your javascript project.
- Use as needed, i.e
  ```
       import HealthData from src/data/index

       const heartRateData = HealthData.HeartRate;
       heartRateData.forEach(heartRate => console.log(heartRate.value));
  ```

##### To convert the XML to grouped JSON only

- Pass the `--json` argument to the script when running
  - `python3 main.py --json`

#### To have more custom configuration

- Update `main.py` as you see fit, to only run certain scripts or not.
