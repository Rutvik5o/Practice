<%@ Page Language="C#" AutoEventWireup="true"  CodeFile="Default.aspx.cs" Inherits="_Default" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Untitled Page</title>
</head>
<body>
    <p>
        Select Products:</p>
    <p>
        &nbsp;</p>
    <form id="form1" runat="server">
    <p>
        <asp:CheckBoxList ID="CheckBoxList1" runat="server" AutoPostBack="True" 
            RepeatDirection="Horizontal">
            <asp:ListItem>Motherboard</asp:ListItem>
            <asp:ListItem>Keyboard</asp:ListItem>
            <asp:ListItem>Modem</asp:ListItem>
            <asp:ListItem>Speaker</asp:ListItem>
            <asp:ListItem>Display</asp:ListItem>
            <asp:ListItem>CPU</asp:ListItem>
        </asp:CheckBoxList>
    </p>
    <p>
        &nbsp;</p>
    <p>
        <asp:Button ID="Button2" runat="server" onclick="Button2_Click" Text="Submit" />
    </p>
    <p>
        &nbsp;</p>
    <p>
        <asp:Label ID="Label1" runat="server" Text="Label"></asp:Label>
    </p>
    <p>
        &nbsp;</p>
    <p>
        &nbsp;</p>
    <div>
    
    </div>
    </form>
</body>
</html>
