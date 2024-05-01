from pprint import pprint
from Questgen import main
qg = main.QGen()
payload = {"input_text": "A recession is an economic term that refers to a significant decline in economic activity across the economy, typically measured by indicators like GDP (Gross Domestic Product), employment rates, industrial production, and consumer spending. During a recession, businesses produce less, unemployment rates rise, incomes decline, and consumer spending decreases. This can lead to a vicious cycle where reduced spending further depresses economic activity.A recession is usually characterized by negative GDP growth for two consecutive quarters or more. However, other factors such as employment rates, industrial production, and consumer confidence also play a role in defining a recession.Governments and central banks often implement various fiscal and monetary policies to try to mitigate the negative effects of a recession, such as reducing interest rates, increasing government spending, and implementing tax cuts."}

output = qg.predict_mcq(payload)
pprint(output)