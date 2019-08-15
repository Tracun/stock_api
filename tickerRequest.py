import gspread
from oauth2client.service_account import ServiceAccountCredentials
from tickerObj import TickerObj
from responseConverter import ResponseConverter

class TickerRequest:

    SHEET_NAME = 'TestePython'
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('./data/client_secret.json', scope)
    client = gspread.authorize(creds)

    def __init__(self):
        pass

    def getTickers(self):

        global client
        global responseConverter
        global SHEET_NAME

        responseConverter = ResponseConverter()
        try:
            sheet = self.client.open(self.SHEET_NAME).sheet1
        except Exception as e:
            return responseConverter.jsonInternalError(e)

        #Obtem os valores da selecao abaixo
        cell_list = sheet.range('d2:k992')
        tickerList = []

        try:
            for x in range(0, len(cell_list), 8):

                if cell_list[x].value == '':
                    break
                else:
                    tickerObj = TickerObj(cell_list[x].value, cell_list[x+1].value, cell_list[x+2].value, cell_list[x+3].value,
                            cell_list[x+4].value, cell_list[x+5].value, cell_list[x+6].value, cell_list[x+7].value)

                    #add obj to list
                    tickerList.append(tickerObj)

            #Return the obj to dict
            results = [obj.to_dict() for obj in tickerList]

            #sort it based on ticker
            results.sort(key=lambda obj: obj["ticker"])

            return responseConverter.tickers(results)
        except Exception as e:
            print('Erro: ', e)

    def getTicker(self, ticker):
        global client
        global responseConverter
        global SHEET_NAME

        responseConverter = ResponseConverter()
        ticker.upper()

        try:
            sheet = self.client.open(self.SHEET_NAME).sheet1
        except Exception as e:
            return responseConverter.jsonInternalError(e)

        try:
            cell = sheet.find(ticker.upper())

            price = sheet.cell(cell.row, 5).value
            changePct = sheet.cell(cell.row, 6).value
            volume = sheet.cell(cell.row, 7).value
            currency = sheet.cell(cell.row, 8).value
            high = sheet.cell(cell.row, 9).value
            low = sheet.cell(cell.row, 10).value
            dataDelay = sheet.cell(cell.row, 11).value

            tickerObj = TickerObj(ticker, price, changePct, volume,
                    currency, high, low, dataDelay)

            return responseConverter.ticker(tickerObj.to_dict())

        except Exception as notFound:
            return responseConverter.tickerNotFound(ticker)

    def newTicker(self, ticker):
        global client
        global responseConverter
        global SHEET_NAME

        responseConverter = ResponseConverter()
        ticker.upper()

        try:
            sheet = self.client.open(self.SHEET_NAME).sheet1
        except Exception as e:
            return responseConverter.jsonInternalError(e)

        try:

            cell = sheet.find(ticker.upper())
            return responseConverter.tickerAlreadyExists(ticker)

        except Exception as notFound:
            #TERMINAR, SE DER ERRO, SIGNIFICA QUE NAO EXISTE, ENTAO VAMOS CRIAR
            line = int(sheet.acell('B12').value)
            cellToInsert = 'D{}'.format(line)

            sheet.update_acell(cellToInsert, ticker)

            #check if the ticket is valid
            if(str(sheet.acell('H{}'.format(line)).value) == 'Not found'):
                sheet.update_acell(cellToInsert, '')
                return responseConverter.tickerNotExists(ticker)

            #update the number of tickers registered
            line += 1
            sheet.update_acell('B12', str(line))
            return responseConverter.tickerCreated(ticker)