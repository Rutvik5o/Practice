<%@ Page Language="C#" AutoEventWireup="true"  CodeFile="Default.aspx.cs" Inherits="_Default" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Untitled Page</title>
</head>
<body>
    <form id="form1" runat="server">
    <p>
        Select Items you want to purchase:</p>
    <p>
        &nbsp;</p>
    <p>
        <asp:CheckBoxList ID="CheckBoxList1" runat="server">
            <asp:ListItem>MotherBoard</asp:ListItem>
            <asp:ListItem>KeyBoard</asp:ListItem>
            <asp:ListItem>Monitor</asp:ListItem>
            <asp:ListItem>CPU</asp:ListItem>
            <asp:ListItem>Graphics Card</asp:ListItem>
            <asp:ListItem>Firmware</asp:ListItem>
        </asp:CheckBoxList>
    </p>
    <p>
        <asp:Button ID="Button1" runat="server" onclick="Button1_Click1" 
            Text="Place Order" />
    </p>
    <p>
        &nbsp;</p>
    <p>
        <asp:Label ID="Label1" runat="server" Text="cart"></asp:Label>
    </p>
</form>
<p>
    &nbsp;</p>
</body>
</html>
