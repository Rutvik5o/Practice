﻿<%@ Page Language="C#" AutoEventWireup="true" CodeFile="Default.aspx.cs" Inherits="_Default" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Untitled Page</title>
</head>
<body>
    <form id="form1" runat="server">
    <p>
        Select File :
        <asp:FileUpload ID="FileUpload1" runat="server" />
    </p>
    <p>
        &nbsp;</p>
    <p>
        <asp:Button ID="Button1" runat="server" onclick="Button1_Click" 
            Text="Insert image" />
    </p>
    <p>
        &nbsp;</p>
    <p>
        &nbsp;</p>
    <p>
        <asp:DataList ID="DataList1" runat="server" RepeatColumns="5" 
            RepeatDirection="Horizontal">
            <ItemTemplate>
                <asp:Image ID="Image1" runat="server" Height="215px" 
                    ImageUrl='<%# Eval("Name","~/images/{0}") %>' Width="229px" />
            </ItemTemplate>
        </asp:DataList>
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
