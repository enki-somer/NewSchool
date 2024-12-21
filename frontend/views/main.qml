import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    visible: true
    width: 1024
    height: 768
    title: "School Management System"

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 10

        Text {
            text: "School Management System"
            font.pixelSize: 24
            Layout.alignment: Qt.AlignHCenter
        }
    }
}