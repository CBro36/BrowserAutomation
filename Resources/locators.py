from selenium.webdriver.common.by import By

#Contains Locators for each page as needed

class AddRemoveLocators():
    AddButton = (By.XPATH, '//*[@id="content"]/div/button')
    DeleteButton = (By.CLASS_NAME, "added-manually")

class BrokenImageLocators():
    Images = (By.CSS_SELECTOR, "img")

class ChallengingDOMLocators():
    Button = (By.CLASS_NAME, "button")
    TableElement = (By.XPATH, '//*[@id="content"]/div/div/div/div[2]/table/tbody/tr[3]/td[2]')
    CanvasScript = (By.XPATH, '//*[@id="content"]/script')

class CheckboxesLocators():
    Checkbox1 = (By.XPATH, '//*[@id="checkboxes"]/input[1]')
    Checkbox2 = (By.XPATH, '//*[@id="checkboxes"]/input[2]')

class ContextMenuLocators():
    Box = (By.ID, 'hot-spot')

class DisappearingElementsLocators():
    GalleryButton = (By.XPATH, '//*[@id="content"]/div/ul/li[5]/a')

class DragAndDropLocators():
    aColumn = (By.ID, "column-a")
    bColumn = (By.ID, "column-b")

class DropdownLocators():
    Dropdown = (By.ID, "dropdown")

class DynamicContentLocators():
    Image = (By.XPATH, '//*[@id="content"]/div[3]/div[1]/img')
    Text = (By.XPATH, '//*[@id="content"]/div[3]/div[2]')

class DynamicControlsLocators():
    Checkbox1 = (By.CSS_SELECTOR, '#checkbox > input')
    Checkbox2 = (By.ID, 'checkbox')
    AddRemove = (By.CSS_SELECTOR, '#checkbox-example > button')
    TextInput = (By.CSS_SELECTOR, '#input-example > input')
    EnableDisable = (By.CSS_SELECTOR, '#input-example > button')
    LoadingBar = (By.ID, 'loading')

class DynamicLoadingLocators():
    Start = (By.CSS_SELECTOR, '#start > button')
    LoadingBar = (By.ID, 'loading')
    Finish = (By.ID, 'finish')

class EntryAdLocators():
    Close = (By.XPATH, '//*[@id="modal"]/div[2]/div[3]/p')
    ModalWindow = (By.ID, 'modal')
    OpenAd = (By.ID, 'restart-ad')

class ExitIntentLocators():
    Close = (By.XPATH, '//*[@id="ouibounce-modal"]/div[2]/div[3]/p')
    Title = (By.CSS_SELECTOR, 'h3')
    ModalWindow = (By.ID, 'ouibounce-modal')

class FileDownloadLocators():
    File1 = (By.XPATH, '//*[@id="content"]/div/a[1]')
    File2 = (By.XPATH, '//*[@id="content"]/div/a[2]')
    File3 = (By.XPATH, '//*[@id="content"]/div/a[3]')
    File4 = (By.XPATH, '//*[@id="content"]/div/a[4]')

class FileUploadLocators():
    ChooseFile = (By.ID, 'file-upload')
    UploadButton = (By.ID, 'file-submit')
    UploadedFile = (By.ID, 'uploaded-files')

class FloatingMenuLocators():
    HomeButton = (By.XPATH, '//*[@id="menu"]/ul/li[1]/a')
    NewsButton = (By.XPATH, '//*[@id="menu"]/ul/li[2]/a')
    ContactButton = (By.XPATH, '//*[@id="menu"]/ul/li[3]/a')
    AboutButton = (By.XPATH, '//*[@id="menu"]/ul/li[4]/a')

class ForgotPasswordLocators():
    EmailInput = (By.ID, 'email')
    SubmitButton = (By.CSS_SELECTOR, '#form_submit > i')

class FormAuthenticationLocators():
    Username = (By.ID, 'username')
    Password = (By.ID, 'password')
    LoginButton = (By.CSS_SELECTOR, '#login > button > i')
    Message = (By.ID, 'flash')
    LogoutButton = (By.CSS_SELECTOR, '#content > div > a > i')

class GeolocationLocators():
    Button = (By.CSS_SELECTOR, '#content > div > button')
    Latitude = (By.ID, 'lat-value')
    Longitude = (By.ID, 'long-value')

class HorizontalSliderLocators():
    Slider = (By.XPATH, '//*[@id="content"]/div/div/input')
    Value = (By.ID, 'range')

class HoversLocators():
    Image1 = (By.XPATH, '//*[@id="content"]/div/div[1]/img')
    Image2 = (By.XPATH, '//*[@id="content"]/div/div[2]/img')
    Image3 = (By.XPATH, '//*[@id="content"]/div/div[3]/img')
    Caption1 = (By.XPATH, '//*[@id="content"]/div/div[1]/div/h5')
    Caption2 = (By.XPATH, '//*[@id="content"]/div/div[2]/div/h5')
    Caption3 = (By.XPATH, '//*[@id="content"]/div/div[3]/div/h5')
    Link1 = (By.XPATH, '//*[@id="content"]/div/div[1]/div/a')
    Link2 = (By.XPATH, '//*[@id="content"]/div/div[2]/div/a')
    Link3 = (By.XPATH, '//*[@id="content"]/div/div[3]/div/a')
    Message = (By.CSS_SELECTOR, 'html > body > h1')

class InfiniteScrollLocators():
    Segments = (By.CLASS_NAME, 'jscroll-added')

class InputLocators():
    InputField = (By.CSS_SELECTOR, '#content > div > div > div > input')

class JQueryUIMenuLocators():
    DButton = (By.ID, 'ui-id-1')
    InvisButton = (By.ID, 'ui-id-2')
    EButton = (By.ID, 'ui-id-3')
    Downloads = (By.ID, 'ui-id-4')
    PDFLink = (By.ID, 'ui-id-5')
    CSVLink = (By.ID, 'ui-id-6')
    ExcelLink = (By.ID, 'ui-id-7')
    BackToJQ = (By.ID, 'ui-id-8')

class JavaScriptAlertsLocators():
    JSAlert = (By.XPATH, '//*[@id="content"]/div/ul/li[1]/button')
    JSConfirm = (By.XPATH, '//*[@id="content"]/div/ul/li[2]/button')
    JSPrompt = (By.XPATH, '//*[@id="content"]/div/ul/li[3]/button')
    Result = (By.ID, 'result')

class KeyPressesLocators():
    Target = (By.ID, 'target')
    Result = (By.ID, 'result')

class LargeAndDeepDOMLocators():
    Sib25_3 = (By.ID, 'sibling-25.3')
    Sib50_2 = (By.ID, 'sibling-50.2')
    TableElem = (By.XPATH, '//*[@id="large-table"]/tbody/tr[47]/td[12]')

class MultipleWindowsLocators():
    Link = (By.CSS_SELECTOR, '#content > div > a')
    Message = (By.CSS_SELECTOR, 'html > body > div > h3')

class NestedFramesLocators():
    Left = (By.CSS_SELECTOR, 'html > body')
    Middle = (By.ID, 'content')
    Right = (By.CSS_SELECTOR, 'html > body')
    Bottom = (By.CSS_SELECTOR, 'html > body')

class NotificationMessageLocators():
    Message = (By.ID, 'flash')
    Link = (By.CSS_SELECTOR, '#content > div > p > a')

class SecureDownloadLocators():
    File1 = (By.XPATH, '//*[@id="content"]/div/a[1]')
    File2 = (By.XPATH, '//*[@id="content"]/div/a[2]')
    File3 = (By.XPATH, '//*[@id="content"]/div/a[3]')
    File4 = (By.XPATH, '//*[@id="content"]/div/a[4]')

class ShadowDOMLocators():
    ShadowHost1 = (By.XPATH, '//*[@id="content"]/my-paragraph[1]')
    RealText = (By.NAME, 'my-text')
    Shadowhost2 = (By.XPATH, '//*[@id="content"]/my-paragraph[2]')
    ListElem1 = (By.XPATH, '//*[@id="content"]/my-paragraph[2]/ul/li[1]')
    ListElem2 = (By.XPATH, '//*[@id="content"]/my-paragraph[2]/ul/li[2]')

class ShiftingMenuLocators():
    Gallery = (By.XPATH, '//*[@id="content"]/div/ul/li[5]/a')

class ShiftingImageLocators():
    Image = (By.CSS_SELECTOR, '#content > div > img')

class ShiftingListLocators():
    List = (By.CSS_SELECTOR, '#content > div > div > div')

class DataTablesLocators():
    Table1 = (By.ID, 'table1')
    Tbody = (By.TAG_NAME, 'tbody')
    Trows = (By.TAG_NAME, 'tr')
    Tdata = (By.TAG_NAME, 'td')
    LastNames = (By.CLASS_NAME, 'last-name')
    FirstNames = (By.CLASS_NAME, 'first-name')
    Emails = (By.CLASS_NAME, 'email')
    Dues = (By.CLASS_NAME, 'dues')
    Sites = (By.CLASS_NAME, 'web-site')
    EditButton = (By.XPATH, '//*[@id="table1"]/tbody/tr[1]/td[6]/a[1]')
    DeleteButton = (By.XPATH, '//*[@id="table2"]/tbody/tr[2]/td[6]/a[2]')

class StatusCodesLocators():
    Link200 = (By.XPATH, '//*[@id="content"]/div/ul/li[1]/a')
    Link301 = (By.XPATH, '//*[@id="content"]/div/ul/li[2]/a')
    Link404 = (By.XPATH, '//*[@id="content"]/div/ul/li[3]/a')
    Link500 = (By.XPATH, '//*[@id="content"]/div/ul/li[4]/a')

class TyposLocators():
    TextBody = (By.CLASS_NAME, 'example')

class WYSIWYGEditorLocators():
    Editor = (By.ID, 'mce_0_ifr')
    TextBox = (By.ID, 'tinymce')
    Bold = (By.XPATH, '//*[@id="content"]/div/div/div[1]/div[1]/div[2]/div/div[3]/button[1]')
    Italics = (By.XPATH, '//*[@id="content"]/div/div/div[1]/div[1]/div[2]/div/div[3]/button[2]')
    AlignCenter = (By.XPATH, '//*[@id="content"]/div/div/div[1]/div[1]/div[2]/div/div[4]/button[2]')
    Indent = (By.XPATH, '//*[@id="content"]/div/div/div[1]/div[1]/div[2]/div/div[5]/button[2]')
    Undo = (By.XPATH, '//*[@id="content"]/div/div/div[1]/div[1]/div[2]/div/div[1]/button[1]')
    Redo = (By.XPATH, '//*[@id="content"]/div/div/div[1]/div[1]/div[2]/div/div[1]/button[2]')
    Formats = (By.XPATH, '//*[@id="content"]/div/div/div[1]/div[1]/div[2]/div/div[2]/button')
    Headings = (By.XPATH, '//*[starts-with(@id, "aria-owns")]/div/div[1]/div/div[1]')
    Heading2 = (By.XPATH, '//*[starts-with(@id, "aria-owns")]/div/div[2]/div/div[2]')